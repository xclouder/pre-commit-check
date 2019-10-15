# -*- coding: utf-8 -*
#!/usr/bin/python
import sys

def validate_line(lineStr):
	if (l.find("Debug.LogError") >= 0 or l.find("Debug.LogDebug") >= 0 or l.find("Debug.LogWarning") >= 0 or 
		l.find("Debug.LogErrorFormat") >= 0 or l.find("Debug.LogDebugFormat") >= 0 or l.find("Debug.LogWarningFormat") >= 0):
		return False

	return True

def validate_json(jsonStr):
	# try:
	# 	json_object = json.loads(myjson)
	# except e:
	# 	sys.stderr.write(e)
	# 	return False
	# return True
	return True

def print_err_msg(filePath, lineNum, line):
	sys.stderr.write(filePath + ":" + str(lineNum) + "\n")
	sys.stderr.write(line)

def print_err_msg_with_info(filePath, info):
	sys.stderr.write(filePath + ":" + info)

if __name__=="__main__":
	retCode = 0

	changedFileDesPath = sys.argv[1]

	with open(changedFileDesPath, 'r') as f:
		try:
			fileList = f.read().splitlines()

			for fPath in fileList:
				if (fPath.endswith(".cs")):
					with open(fPath, 'r') as codeFile:
						lines = codeFile.read().splitlines()

						lnNum = 0
						for ln in lines:
							lnNum = lnNum + 1
							l = ln.lstrip()
							if (not validate_line(l)):
								print_err_msg(fPath, lnNum, l)
								retCode = 1

				if (fPath.endswith(".json")):
					# validate json format
					with open(fPath, 'r') as codeFile:
						jsonStr = codeFile.read()

						if (not validate_json(jsonStr)):
							print_err_msg_with_info(fPath, "invalid json file")
							retCode = 1

		except:
			sys.stderr.write("open file error:" + changedFileDesPath)

	exit(retCode)