# TF::AWS::PinpointApp CampaignHookDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lambdafunctionname" title="LambdaFunctionName">LambdaFunctionName</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#weburl" title="WebUrl">WebUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#lambdafunctionname" title="LambdaFunctionName">LambdaFunctionName</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#weburl" title="WebUrl">WebUrl</a>: <i>String</i>
</pre>

## Properties

#### LambdaFunctionName

Lambda function name or ARN to be called for delivery. Conflicts with `web_url`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebUrl

Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

