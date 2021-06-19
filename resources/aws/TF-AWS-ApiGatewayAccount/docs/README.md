# TF::AWS::ApiGatewayAccount

Provides a settings of an API Gateway Account. Settings is applied region-wide per `provider` block.

-> **Note:** As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApiGatewayAccount",
    "Properties" : {
        "<a href="#cloudwatchrolearn" title="CloudwatchRoleArn">CloudwatchRoleArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApiGatewayAccount
Properties:
    <a href="#cloudwatchrolearn" title="CloudwatchRoleArn">CloudwatchRoleArn</a>: <i>String</i>
</pre>

## Properties

#### CloudwatchRoleArn

The ARN of an IAM role for CloudWatch (to allow logging & monitoring). See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console). Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

_Required_: No

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

#### ThrottleSettings

Returns the <code>ThrottleSettings</code> value.

