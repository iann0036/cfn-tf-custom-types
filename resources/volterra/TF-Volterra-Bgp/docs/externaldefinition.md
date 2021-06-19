# TF::Volterra::Bgp ExternalDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>" : <i>Boolean</i>,
    "<a href="#fromsite" title="FromSite">FromSite</a>" : <i>Boolean</i>,
    "<a href="#insideinterfaces" title="InsideInterfaces">InsideInterfaces</a>" : <i>Boolean</i>,
    "<a href="#outsideinterfaces" title="OutsideInterfaces">OutsideInterfaces</a>" : <i>Boolean</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#subnetbeginoffset" title="SubnetBeginOffset">SubnetBeginOffset</a>" : <i>Double</i>,
    "<a href="#subnetendoffset" title="SubnetEndOffset">SubnetEndOffset</a>" : <i>Double</i>,
    "<a href="#familyinet" title="FamilyInet">FamilyInet</a>" : <i>[ <a href="familyinetdefinition.md">FamilyInetDefinition</a>, ... ]</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
    "<a href="#interfacelist" title="InterfaceList">InterfaceList</a>" : <i>[ <a href="interfacelistdefinition.md">InterfaceListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>: <i>Boolean</i>
<a href="#fromsite" title="FromSite">FromSite</a>: <i>Boolean</i>
<a href="#insideinterfaces" title="InsideInterfaces">InsideInterfaces</a>: <i>Boolean</i>
<a href="#outsideinterfaces" title="OutsideInterfaces">OutsideInterfaces</a>: <i>Boolean</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#subnetbeginoffset" title="SubnetBeginOffset">SubnetBeginOffset</a>: <i>Double</i>
<a href="#subnetendoffset" title="SubnetEndOffset">SubnetEndOffset</a>: <i>Double</i>
<a href="#familyinet" title="FamilyInet">FamilyInet</a>: <i>
      - <a href="familyinetdefinition.md">FamilyInetDefinition</a></i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
<a href="#interfacelist" title="InterfaceList">InterfaceList</a>: <i>
      - <a href="interfacelistdefinition.md">InterfaceListDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromSite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideInterfaces

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideInterfaces

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetBeginOffset

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetEndOffset

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FamilyInet

_Required_: No

_Type_: List of <a href="familyinetdefinition.md">FamilyInetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceList

_Required_: No

_Type_: List of <a href="interfacelistdefinition.md">InterfaceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

