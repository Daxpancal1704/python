from pathlib import Path

class UnsupportedOperatorError(Exception):
    """Rais when a user provides an operator is not in  supporeted list"""


def safe_calu():
 
    BASE_URL=Path(__file__).parent
    FILE_NAME=BASE_URL / "ans.txt"

    supported_list={"+", "-", "*", "/", "%", "//", "**"}
    history=[]
    attempts=0


    print('Safe commandline calculator')
    print("enter your expression like this ex .. 10 + 12    (not supported like 1 + 2 - 3 )  ")
    print("enter 'q' and exit ")

    while True:
        try:
                user_exp=input("Enter your expre >> ")
                if user_exp.lower() == "q":
                    print("\n Exit calcuator")
                    break

                if not  user_exp:
                    continue

                attempts += 1

                part=user_exp.split()
                if len(part) != 3:
                    raise ValueError("formate must be correct")

                num1, operator, num2 = part

                if operator not in supported_list:
                    raise UnsupportedOperatorError(f"operstor {operator} not supported")
                nums1=float(num1)
                nums2=float(num2)


                if nums1.is_integer():nums1=int(nums1)
                if nums2.is_integer():nums2=int(nums2)


                if operator == "+": result =nums1+nums2
                elif operator == "-":  result =nums1 - nums2 
                elif operator == "*": result =nums1 * nums2 
                elif operator == "/": result =nums1 / nums2 
                elif operator == "//": result =nums1 // nums2 
                elif operator == "**": result =nums1 ** nums2 
                elif operator == "%": result =nums1 % nums2 

        except ValueError as e:
                if "could not convert to string to float" in str(e):
                    print("error : operator must be valid number")
                else:
                    print(f"Error: {e}")


        except UnsupportedOperatorError as e:
            print(f"error : {e}")
        
        except ZeroDivisionError:
            print("Error: division or module by zero is not alowed")

        except KeyboardInterrupt:
            print("\n [ctrl + c dected] Exsitinf calculate cleanly..")
            break
        else:
            output_str=f"{num1} {operator} {num2} = {result}"
            print(f"Result : {output_str}")
            history.append(f"{user_exp} -> {output_str}")

        finally:
            if 'user_exp' in locals() and user_exp.lower() != 'q':
                    print(f"--- attempt #{attempts} done ---\n") 

        if history:

            try:
                file_obj=open(FILE_NAME,"a",encoding="utf-8")
                for record in history:
                        file_obj.write(record +"\n")
                file_obj.close()
                print(f"session history succesfully sae {FILE_NAME}")
            except Exception as e:
                print(f"failed to write  history files : {e}")

if __name__=="__main__":
    try:
        safe_calu()
    except KeyboardInterrupt:
        print("\n Calculator terminated before initializations")
