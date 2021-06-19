# TF::Vultr::LoadBalancer ForwardingRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
    "<a href="#backendprotocol" title="BackendProtocol">BackendProtocol</a>" : <i>String</i>,
    "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>Double</i>,
    "<a href="#frontendprotocol" title="FrontendProtocol">FrontendProtocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
<a href="#backendprotocol" title="BackendProtocol">BackendProtocol</a>: <i>String</i>
<a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>Double</i>
<a href="#frontendprotocol" title="FrontendProtocol">FrontendProtocol</a>: <i>String</i>
</pre>

## Properties

#### BackendPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

