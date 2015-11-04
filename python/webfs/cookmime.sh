cat mime.types | awk '{print $2}' | sed 's/;//' | sed 's/{//' | sed '/^\s*$/d' > mime.new.types
