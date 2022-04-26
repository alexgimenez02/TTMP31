#!/bin/sh

# Also see https://www.jython.org/jython-old-sites/archive/21/docs/interpreter.html

# updated to Jython 2.7.2 (final release)
# also with imgscalr – Java Image Scaling Library
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -Dpython.console=org.python.util.JLineConsole -classpath "./library:./library/jython2.7.2/jython.jar:./library/jython2.7.2/Lib:./library/jMusic1.7/inst:./library/jMusic1.7/jmusic.jar:./library/jsyn/jsyn.jar:./library/imgscalr-lib-4.2/imgscalr-lib-4.2.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "-u" "$@"
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -Dpython.console=org.python.util.PlainConsole -classpath "./library:./library/jython2.7.2/jython.jar:./library/jython2.7.2/Lib:./library/jMusic1.7/inst:./library/jMusic1.7/jmusic.jar:./library/jsyn/jsyn.jar:./library/imgscalr-lib-4.2/imgscalr-lib-4.2.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "-u" "$@" "-c" "exit()"
java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -classpath "./library:./library/jython2.7.2/jython.jar:./library/jython2.7.2/Lib:./library/jMusic1.7/inst:./library/jMusic1.7/jmusic.jar:./library/jsyn/jsyn.jar:./library/imgscalr-lib-4.2/imgscalr-lib-4.2.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "-u" "$@"

# using jMusic 1.7.0 with Gervill and Java 6 - see http://stackoverflow.com/questions/7749172/why-java-midi-synth-on-mac-stop-playing-notes
# also with imgscalr – Java Image Scaling Library
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.7/inst:./library/jMusic1.7/jmusic.jar:./library/jsyn/jsyn.jar:./library/imgscalr-lib-4.2/imgscalr-lib-4.2.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "$@"

# using jMusic 1.7.0 with Java 7
#java -Xmx4096m -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.7/inst:./library/jMusic1.7/jmusic.jar:./library/jsyn/jsyn.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "$@"

# using jMusic 1.7.0 with Gervill and Java 6 - see http://stackoverflow.com/questions/7749172/why-java-midi-synth-on-mac-stop-playing-notes
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.7/inst:./library/jMusic1.7/jmusic.jar:./library/jsyn/jsyn.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "$@"

# Using Gervill with Java 6 - see http://stackoverflow.com/questions/7749172/why-java-midi-synth-on-mac-stop-playing-notes
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "$@"

# using jMusic 1.6.4
#java -Xmx4096m -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "$@"

# Using Gervill with Java 6 - see http://stackoverflow.com/questions/7749172/why-java-midi-synth-on-mac-stop-playing-notes
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:./library/javaosc-core.jar${CLASSPATH}" "org.python.util.jython" "$@"

# BACKUP -- Using Gervill with Java 6 - see http://stackoverflow.com/questions/7749172/why-java-midi-synth-on-mac-stop-playing-notes
#java -Xmx4096m -Dsun.sound.useNewAudioEngine=true -Dpython.home="." -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:${CLASSPATH}" "org.python.util.jython" "$@"

#java -Xmx4096m -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:${CLASSPATH}" "org.python.util.jython" "$@"

#java -Xmx4096m -Dpython.home="./library/jython2.5.3" -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:${CLASSPATH}" "org.python.util.jython" "$@"

#java -Xmx4096m -Dpython.home="./library" -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:${CLASSPATH}" "org.python.util.jython" "$@"

#java -Xmx4096m -Dpython.home="./library" -Dpython.console=org.python.util.InteractiveConsole -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:${CLASSPATH}" "org.python.util.jython" "$@"

#java -Xmx2048m -Dpython.home="./library" -classpath "./library:./library/jython2.5.3/jython.jar:./library/jython2.5.3/Lib:./library/jMusic1.6.4/inst:./library/jMusic1.6.4/jmusic.jar:./library/jsyn/jsyn.jar:${CLASSPATH}" "org.python.util.jython" "$@"
