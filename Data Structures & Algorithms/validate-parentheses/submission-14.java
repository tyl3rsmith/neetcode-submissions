class Solution {
    // if we get an opening bracket push it onto the stack
    // if we get a closing bracket check if it matches the previous bracket
    // if there is no previous bracket i.e. the stack is empty return false
    // or if there is a mismatch return false
    // repeat until we've exhausted all characters
    // if the stack is empty at the end return true

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put(')', '(');
        closeToOpen.put(']', '[');
        closeToOpen.put('}', '{');

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.peek() != closeToOpen.get(c)) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
