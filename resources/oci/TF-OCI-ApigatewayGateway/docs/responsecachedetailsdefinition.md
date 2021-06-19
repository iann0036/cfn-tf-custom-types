# TF::OCI::ApigatewayGateway ResponseCacheDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationsecretid" title="AuthenticationSecretId">AuthenticationSecretId</a>" : <i>String</i>,
    "<a href="#authenticationsecretversionnumber" title="AuthenticationSecretVersionNumber">AuthenticationSecretVersionNumber</a>" : <i>String</i>,
    "<a href="#connecttimeoutinms" title="ConnectTimeoutInMs">ConnectTimeoutInMs</a>" : <i>Double</i>,
    "<a href="#issslenabled" title="IsSslEnabled">IsSslEnabled</a>" : <i>Boolean</i>,
    "<a href="#issslverifydisabled" title="IsSslVerifyDisabled">IsSslVerifyDisabled</a>" : <i>Boolean</i>,
    "<a href="#readtimeoutinms" title="ReadTimeoutInMs">ReadTimeoutInMs</a>" : <i>Double</i>,
    "<a href="#sendtimeoutinms" title="SendTimeoutInMs">SendTimeoutInMs</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#servers" title="Servers">Servers</a>" : <i>[ <a href="serversdefinition.md">ServersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationsecretid" title="AuthenticationSecretId">AuthenticationSecretId</a>: <i>String</i>
<a href="#authenticationsecretversionnumber" title="AuthenticationSecretVersionNumber">AuthenticationSecretVersionNumber</a>: <i>String</i>
<a href="#connecttimeoutinms" title="ConnectTimeoutInMs">ConnectTimeoutInMs</a>: <i>Double</i>
<a href="#issslenabled" title="IsSslEnabled">IsSslEnabled</a>: <i>Boolean</i>
<a href="#issslverifydisabled" title="IsSslVerifyDisabled">IsSslVerifyDisabled</a>: <i>Boolean</i>
<a href="#readtimeoutinms" title="ReadTimeoutInMs">ReadTimeoutInMs</a>: <i>Double</i>
<a href="#sendtimeoutinms" title="SendTimeoutInMs">SendTimeoutInMs</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#servers" title="Servers">Servers</a>: <i>
      - <a href="serversdefinition.md">ServersDefinition</a></i>
</pre>

## Properties

#### AuthenticationSecretId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationSecretVersionNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimeoutInMs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSslEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSslVerifyDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadTimeoutInMs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendTimeoutInMs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

_Required_: No

_Type_: List of <a href="serversdefinition.md">ServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

