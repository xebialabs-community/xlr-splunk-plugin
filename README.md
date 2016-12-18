# Preface #

This document describes the functionality provided by the xlr-splunk-plugin.

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/index.html)** for background information on XL Release and release concepts.

# CI status #

[![Build Status][xlr-splunk-plugin-travis-image] ][xlr-splunk-plugin-travis-url]
[![Build Status][xlr-splunk-plugin-codacy-image] ][xlr-splunk-plugin-codacy-url]
[![Build Status][xlr-splunk-plugin-code-climate-image] ][xlr-splunk-plugin-code-climate-url]


[xlr-splunk-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-splunk-plugin.svg?branch=master
[xlr-splunk-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-splunk-plugin
[xlr-splunk-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/8fe65dd028a449fcac5d0d045b5d7fda
[xlr-splunk-plugin-codacy-url]: https://www.codacy.com/app/rvanstone/xlr-splunk-plugin
[xlr-splunk-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xlr-splunk-plugin/badges/gpa.svg
[xlr-splunk-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xlr-splunk-plugin


# Overview #

The xlr-splunk-plugin is an XL Release plugin that allows to use the export hook to send logs to Splunk.

# Usage #
Create an instance of the export hook according to the [XLR documentation](https://docs.xebialabs.com/xl-release/how-to/create-an-export-hook.html).

# Remark #

If you wish to send the complete XL Release log file to Splunk, you can use the following documentation to configure the XL Release logback system.
This is based on [Splunk logging Java](http://dev.splunk.com/view/splunk-logging-java/SP-CAAAE2K)
You will also have to put the following jar file into the `lib` folder:
+ [splunk-library-java-logging](http://dev.splunk.com/goto/loggingjavajar)

See: 
+ TCP: http://dev.splunk.com/view/splunk-logging-java/SP-CAAAE3R
  ```
    <configuration>
        <appender name="socket" class="com.splunk.logging.TcpAppender">
            <RemoteHost>127.0.0.1</RemoteHost>
            <Port>15000</Port>
            <layout class="ch.qos.logback.classic.PatternLayout">
            <pattern>%date{ISO8601} [%thread] %level: %msg%n</pattern>
            </layout>
        </appender>
    
        <logger name="splunk.logger" additivity="false" level="INFO">
            <appender-ref ref="socket"/>
        </logger>
    
        <root level="INFO">
            <appender-ref ref="socket"/>
        </root>
    </configuration>
  ```
+ HTTP: http://dev.splunk.com/view/splunk-logging-java/SP-CAAAE7M
  ```
      <configuration>
          <Appender name="%user_logger_name%" class="com.splunk.logging.HttpEventCollectorLogbackAppender">
              <url>%scheme%://%host%:%port%</url>
              <token>%user_httpeventcollector_token%</token>
              <disableCertificateValidation>true</disableCertificateValidation>
              <layout class="ch.qos.logback.classic.PatternLayout">
                  <pattern>%msg</pattern>
              </layout>
          </Appender>
          <logger name ="%user_logger_name%" level="debug">
              <appender-ref ref="%user_logger_name%" />
          </logger>
      </configuration>
  ```
