package model.expression;

import model.state.Heap;
import model.state.SymbolTable;
import model.type.BoolType;
import model.type.IntType;
import model.type.Type;
import model.value.BooleanValue;
import model.value.IntegerValue;
import model.value.Value;
import exceptions.ExpressionEvaluationException;

public record BinaryOperatorExpression(String operator, Expression left, Expression right) implements Expression {

    @Override
    public Value evaluate(SymbolTable symTable, Heap heap) {
        var leftTerm = left.evaluate(symTable, heap);
        var rightTerm = right.evaluate(symTable, heap);

        switch (operator) {
            case "+", "-", "*", "/" -> {
                checkTypes(leftTerm, rightTerm, new IntType());
                var leftValue = (IntegerValue) leftTerm;
                var rightValue = (IntegerValue) rightTerm;
                return evaluateArithmeticExpression(leftValue, rightValue);
            }
            case "&&", "||" -> {
                checkTypes(leftTerm, rightTerm, new BoolType());
                var leftValueB = (BooleanValue) leftTerm;
                var rightValueB = (BooleanValue) rightTerm;
                return evaluateBooleanExpression(leftValueB, rightValueB);
            }
            case "<", "<=", "==", "!=", ">", ">=" -> {
                checkTypes(leftTerm, rightTerm, new IntType());
                var leftInt = (IntegerValue) leftTerm;
                var rightInt = (IntegerValue) rightTerm;
                return switch (operator) {
                    case "<"  -> new BooleanValue(leftInt.value() <  rightInt.value());
                    case "<=" -> new BooleanValue(leftInt.value() <= rightInt.value());
                    case "==" -> new BooleanValue(leftInt.value() == rightInt.value());
                    case "!=" -> new BooleanValue(leftInt.value() != rightInt.value());
                    case ">"  -> new BooleanValue(leftInt.value() >  rightInt.value());
                    case ">=" -> new BooleanValue(leftInt.value() >= rightInt.value());
                    default   -> throw new ExpressionEvaluationException("Invalid relational operator: " + operator);
                };
            }
        }

        throw new ExpressionEvaluationException("Unknown operator: " + operator);
    }

    private void checkTypes(Value leftTerm, Value rightTerm, Type expectedType) {
        if (!leftTerm.getType().equals(expectedType) || !rightTerm.getType().equals(expectedType)) {
            throw new ExpressionEvaluationException("Wrong types for operator " + operator);
        }
    }

    private IntegerValue evaluateArithmeticExpression(IntegerValue leftValue, IntegerValue rightValue) {
        return switch (operator) {
            case "+" -> new IntegerValue(leftValue.value() + rightValue.value());
            case "-" -> new IntegerValue(leftValue.value() - rightValue.value());
            case "*" -> new IntegerValue(leftValue.value() * rightValue.value());
            case "/" -> {
                if (rightValue.value() == 0) {
                    throw new ExpressionEvaluationException("Division by zero");
                }
                yield new IntegerValue(leftValue.value() / rightValue.value());
            }
            default -> throw new ExpressionEvaluationException("Unreachable code");
        };
    }

    private BooleanValue evaluateBooleanExpression(BooleanValue leftValue, BooleanValue rightValue) {
        return switch (operator) {
            case "&&" -> new BooleanValue(leftValue.value() && rightValue.value());
            case "||" -> new BooleanValue(leftValue.value() || rightValue.value());
            default -> throw new ExpressionEvaluationException("Unreachable code");
        };
    }

    @Override
    public String toString() {
        return "(" + left + " " + operator + " " + right + ")";
    }
}
