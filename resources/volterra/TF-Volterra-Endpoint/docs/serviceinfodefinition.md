# TF::Volterra::Endpoint ServiceInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#discoverytype" title="DiscoveryType">DiscoveryType</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    "<a href="#serviceselector" title="ServiceSelector">ServiceSelector</a>" : <i>[ <a href="serviceselectordefinition.md">ServiceSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#discoverytype" title="DiscoveryType">DiscoveryType</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
<a href="#serviceselector" title="ServiceSelector">ServiceSelector</a>: <i>
      - <a href="serviceselectordefinition.md">ServiceSelectorDefinition</a></i>
</pre>

## Properties

#### DiscoveryType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceSelector

_Required_: No

_Type_: List of <a href="serviceselectordefinition.md">ServiceSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

