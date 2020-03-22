# Terraform::Datadog::SyntheticsTest

Provides a Datadog synthetics test resource. This can be used to create and manage Datadog synthetics test.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::SyntheticsTest",
    "Properties" : {
        "<a href="#assertions" title="Assertions">Assertions</a>" : <i>[ [ <a href="assertions.md">Assertions</a>, ... ], ... ]</i>,
        "<a href="#deviceids" title="DeviceIds">DeviceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ <a href="request.md">Request</a>, ... ]</i>,
        "<a href="#requestheaders" title="RequestHeaders">RequestHeaders</a>" : <i>[ <a href="requestheaders.md">RequestHeaders</a>, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subtype" title="Subtype">Subtype</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::SyntheticsTest
Properties:
    <a href="#assertions" title="Assertions">Assertions</a>: <i>
      - List of <a href="assertions.md">Assertions</a></i>
    <a href="#deviceids" title="DeviceIds">DeviceIds</a>: <i>
      - String</i>
    <a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
    <a href="#request" title="Request">Request</a>: <i>
      - <a href="request.md">Request</a></i>
    <a href="#requestheaders" title="RequestHeaders">RequestHeaders</a>: <i>
      - <a href="requestheaders.md">RequestHeaders</a></i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subtype" title="Subtype">Subtype</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Assertions

Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: No

_Type_: List of List of <a href="assertions.md">Assertions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIds

"laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

A message to include with notifications for this synthetics test.
Email notifications can be sent to specific users by using the same '@username' notation as events.
- `tags` - (Required) A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.
- `request` - (Required) if type=api and subtype=http
- `method` - (Optional) For type=api and subtype=http, one of DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
- `url` - (Required) Any url
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `body` - (Optional) Request body
- `request` - (Required) if type=api and subtype=ssl
- `host` - (Required) host name
- `port` - (Required) port number
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `request` - (Required) if type=browser
- `method` - (Required) no-op, use GET
- `url` - (Required) Any url
- `request_headers` - (Optional) Header name and value map
- `assertions` - (Required) Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Datadog synthetics test
- `message` - (Required) A message to include with notifications for this synthetics test.
Email notifications can be sent to specific users by using the same '@username' notation as events.
- `tags` - (Required) A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.
- `request` - (Required) if type=api and subtype=http
- `method` - (Optional) For type=api and subtype=http, one of DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
- `url` - (Required) Any url
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `body` - (Optional) Request body
- `request` - (Required) if type=api and subtype=ssl
- `host` - (Required) host name
- `port` - (Required) port number
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `request` - (Required) if type=browser
- `method` - (Required) no-op, use GET
- `url` - (Required) Any url
- `request_headers` - (Optional) Header name and value map
- `assertions` - (Required) Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: No

_Type_: List of <a href="options.md">Options</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

if type=browser
- `method` - (Required) no-op, use GET
- `url` - (Required) Any url
- `request_headers` - (Optional) Header name and value map
- `assertions` - (Required) Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: Yes

_Type_: List of <a href="request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaders

Header name and value map
- `assertions` - (Required) Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: No

_Type_: List of <a href="requestheaders.md">RequestHeaders</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

"live", "paused".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subtype

For type=api, http or ssl (Default = http)
- `name` - (Required) Name of Datadog synthetics test
- `message` - (Required) A message to include with notifications for this synthetics test.
Email notifications can be sent to specific users by using the same '@username' notation as events.
- `tags` - (Required) A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.
- `request` - (Required) if type=api and subtype=http
- `method` - (Optional) For type=api and subtype=http, one of DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
- `url` - (Required) Any url
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `body` - (Optional) Request body
- `request` - (Required) if type=api and subtype=ssl
- `host` - (Required) host name
- `port` - (Required) port number
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `request` - (Required) if type=browser
- `method` - (Required) no-op, use GET
- `url` - (Required) Any url
- `request_headers` - (Optional) Header name and value map
- `assertions` - (Required) Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.
- `request` - (Required) if type=api and subtype=http
- `method` - (Optional) For type=api and subtype=http, one of DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
- `url` - (Required) Any url
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `body` - (Optional) Request body
- `request` - (Required) if type=api and subtype=ssl
- `host` - (Required) host name
- `port` - (Required) port number
- `timeout` - (Optional) For type=api, any value between 0 and 60 (Default = 60)
- `request` - (Required) if type=browser
- `method` - (Required) no-op, use GET
- `url` - (Required) Any url
- `request_headers` - (Optional) Header name and value map
- `assertions` - (Required) Array of 1 to 10 items, only some combinations of type/operator are valid (please refer to Datadog documentation)
- `type` - (Required) body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

body, header, responseTime, statusCode
- `operator` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as operator depend on assertion type
- `target` - (Required) Expected value, please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#validation) as target depend on assertion type
- `property` - (Optional) if assertion type is "header", this is a the header name
- `options` - (Required)
- `tick_every` - (Required)  How often the test should run (in seconds). Current possible values are 900, 1800, 3600, 21600, 43200, 86400, 604800 plus 60 if type=api or 300 if type=browser
- `follow_redirects` - (Optional) For type=api, true or false
- `min_failure_duration` - (Optional) How long the test should be in failure before alerting (integer, number of seconds, max 7200). Default is 0.
- `min_location_failed` - (Optional) Threshold below which a synthetics test is allowed to fail before sending notifications
- `accept_self_signed` - (Optional) For type=ssl, true or false
- `locations` - (Required) Please refer to [Datadog documentation](https://docs.datadoghq.com/synthetics/api_test/#request) for available locations (e.g. "aws:eu-central-1")
- `device_ids` - (Optional) "laptop_large", "tablet" or "mobile_small" (only available if type=browser)
- `status` - (Required) "live", "paused".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### MonitorId

Returns the <code>MonitorId</code> value.

