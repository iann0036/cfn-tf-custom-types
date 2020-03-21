# Terraform::Spotinst::ElastigroupGke BackendServices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#locationtype" title="LocationType">LocationType</a>" : <i>String</i>,
    "<a href="#scheme" title="Scheme">Scheme</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    "<a href="#namedports" title="NamedPorts">NamedPorts</a>" : <i>[ &lt;a href=&#34;backendservices-namedports.md&#34;&gt;NamedPorts&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#locationtype" title="LocationType">LocationType</a>: <i>String</i>
<a href="#scheme" title="Scheme">Scheme</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
<a href="#namedports" title="NamedPorts">NamedPorts</a>: <i>
      - &lt;a href=&#34;backendservices-namedports.md&#34;&gt;NamedPorts&lt;/a&gt;</i>
</pre>

## Properties

#### LocationType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheme

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedPorts

_Required_: No
_Type_: List of &lt;a href=&#34;backendservices-namedports.md&#34;&gt;NamedPorts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

