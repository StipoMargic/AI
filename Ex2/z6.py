def check_is_result_zero(lst, num):
  if not lst:
    if num == 0:
      return True
    return False

  if check_is_result_zero(lst[1:], lst[0] + num) or check_is_result_zero(lst[1:], lst[0] - num):
    return True
  return False

print(check_is_result_zero([1,4, 5,2,4], 0))
