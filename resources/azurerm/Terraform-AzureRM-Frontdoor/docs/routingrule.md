# Terraform::AzureRM::Frontdoor RoutingRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptedprotocols" title="AcceptedProtocols">AcceptedProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#frontendendpoints" title="FrontendEndpoints">FrontendEndpoints</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#patternstomatch" title="PatternsToMatch">PatternsToMatch</a>" : <i>[ String, ... ]</i>,
    "<a href="#forwardingconfiguration" title="ForwardingConfiguration">ForwardingConfiguration</a>" : <i>[ <a href="routingrule-forwardingconfiguration.md">ForwardingConfiguration</a>, ... ]</i>,
    "<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>" : <i>[ <a href="routingrule-redirectconfiguration.md">RedirectConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acceptedprotocols" title="AcceptedProtocols">AcceptedProtocols</a>: <i>
      - String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#frontendendpoints" title="FrontendEndpoints">FrontendEndpoints</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#patternstomatch" title="PatternsToMatch">PatternsToMatch</a>: <i>
      - String</i>
<a href="#forwardingconfiguration" title="ForwardingConfiguration">ForwardingConfiguration</a>: <i>
      - <a href="routingrule-forwardingconfiguration.md">ForwardingConfiguration</a></i>
<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>: <i>
      - <a href="routingrule-redirectconfiguration.md">RedirectConfiguration</a></i>
</pre>

## Properties

#### AcceptedProtocols

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendEndpoints

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatternsToMatch

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingConfiguration

_Required_: No

_Type_: List of <a href="routingrule-forwardingconfiguration.md">ForwardingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfiguration

_Required_: No

_Type_: List of <a href="routingrule-redirectconfiguration.md">RedirectConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

