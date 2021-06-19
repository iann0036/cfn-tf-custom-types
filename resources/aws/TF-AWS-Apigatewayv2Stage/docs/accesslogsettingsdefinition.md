# TF::AWS::Apigatewayv2Stage AccessLogSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationarn" title="DestinationArn">DestinationArn</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destinationarn" title="DestinationArn">DestinationArn</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
</pre>

## Properties

#### DestinationArn

The ARN of the CloudWatch Logs log group to receive access logs. Any trailing `:*` is trimmed from the ARN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

A single line [format](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#apigateway-cloudwatch-log-formats) of the access logs of data, as specified by [selected $context variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

