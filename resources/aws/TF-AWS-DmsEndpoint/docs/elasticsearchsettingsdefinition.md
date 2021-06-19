# TF::AWS::DmsEndpoint ElasticsearchSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endpointuri" title="EndpointUri">EndpointUri</a>" : <i>String</i>,
    "<a href="#errorretryduration" title="ErrorRetryDuration">ErrorRetryDuration</a>" : <i>Double</i>,
    "<a href="#fullloaderrorpercentage" title="FullLoadErrorPercentage">FullLoadErrorPercentage</a>" : <i>Double</i>,
    "<a href="#serviceaccessrolearn" title="ServiceAccessRoleArn">ServiceAccessRoleArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#endpointuri" title="EndpointUri">EndpointUri</a>: <i>String</i>
<a href="#errorretryduration" title="ErrorRetryDuration">ErrorRetryDuration</a>: <i>Double</i>
<a href="#fullloaderrorpercentage" title="FullLoadErrorPercentage">FullLoadErrorPercentage</a>: <i>Double</i>
<a href="#serviceaccessrolearn" title="ServiceAccessRoleArn">ServiceAccessRoleArn</a>: <i>String</i>
</pre>

## Properties

#### EndpointUri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorRetryDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullLoadErrorPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccessRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

