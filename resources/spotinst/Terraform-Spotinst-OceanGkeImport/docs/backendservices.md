# Terraform::Spotinst::OceanGkeImport BackendServices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#locationtype" title="LocationType">LocationType</a>" : <i>String</i>,
    "<a href="#scheme" title="Scheme">Scheme</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    "<a href="#namedports" title="NamedPorts">NamedPorts</a>" : <i>[ <a href="backendservices-namedports.md">NamedPorts</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#locationtype" title="LocationType">LocationType</a>: <i>String</i>
<a href="#scheme" title="Scheme">Scheme</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
<a href="#namedports" title="NamedPorts">NamedPorts</a>: <i>
      - <a href="backendservices-namedports.md">NamedPorts</a></i>
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
_Type_: List of <a href="backendservices-namedports.md">NamedPorts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

