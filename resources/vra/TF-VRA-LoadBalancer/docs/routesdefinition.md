# TF::VRA::LoadBalancer RoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthcheckconfiguration" title="HealthCheckConfiguration">HealthCheckConfiguration</a>" : <i>[ <a href="healthcheckconfigurationdefinition.md">HealthCheckConfigurationDefinition</a>, ... ]</i>,
    "<a href="#memberport" title="MemberPort">MemberPort</a>" : <i>String</i>,
    "<a href="#memberprotocol" title="MemberProtocol">MemberProtocol</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#healthcheckconfiguration" title="HealthCheckConfiguration">HealthCheckConfiguration</a>: <i>
      - <a href="healthcheckconfigurationdefinition.md">HealthCheckConfigurationDefinition</a></i>
<a href="#memberport" title="MemberPort">MemberPort</a>: <i>String</i>
<a href="#memberprotocol" title="MemberProtocol">MemberProtocol</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### HealthCheckConfiguration

_Required_: No

_Type_: List of <a href="healthcheckconfigurationdefinition.md">HealthCheckConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberPort

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

