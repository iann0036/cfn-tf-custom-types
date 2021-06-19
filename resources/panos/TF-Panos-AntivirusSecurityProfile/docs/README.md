# TF::Panos::AntivirusSecurityProfile

Manages anti-virus security profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::AntivirusSecurityProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#packetcapture" title="PacketCapture">PacketCapture</a>" : <i>Boolean</i>,
        "<a href="#threatexceptions" title="ThreatExceptions">ThreatExceptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#applicationexception" title="ApplicationException">ApplicationException</a>" : <i>[ <a href="applicationexceptiondefinition.md">ApplicationExceptionDefinition</a>, ... ]</i>,
        "<a href="#decoder" title="Decoder">Decoder</a>" : <i>[ <a href="decoderdefinition.md">DecoderDefinition</a>, ... ]</i>,
        "<a href="#machinelearningexception" title="MachineLearningException">MachineLearningException</a>" : <i>[ <a href="machinelearningexceptiondefinition.md">MachineLearningExceptionDefinition</a>, ... ]</i>,
        "<a href="#machinelearningmodel" title="MachineLearningModel">MachineLearningModel</a>" : <i>[ <a href="machinelearningmodeldefinition.md">MachineLearningModelDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::AntivirusSecurityProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#packetcapture" title="PacketCapture">PacketCapture</a>: <i>Boolean</i>
    <a href="#threatexceptions" title="ThreatExceptions">ThreatExceptions</a>: <i>
      - String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#applicationexception" title="ApplicationException">ApplicationException</a>: <i>
      - <a href="applicationexceptiondefinition.md">ApplicationExceptionDefinition</a></i>
    <a href="#decoder" title="Decoder">Decoder</a>: <i>
      - <a href="decoderdefinition.md">DecoderDefinition</a></i>
    <a href="#machinelearningexception" title="MachineLearningException">MachineLearningException</a>: <i>
      - <a href="machinelearningexceptiondefinition.md">MachineLearningExceptionDefinition</a></i>
    <a href="#machinelearningmodel" title="MachineLearningModel">MachineLearningModel</a>: <i>
      - <a href="machinelearningmodeldefinition.md">MachineLearningModelDefinition</a></i>
</pre>

## Properties

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group location (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketCapture

Set to `true` to enable packet capture.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatExceptions

List of threat exceptions.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys location (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationException

_Required_: No

_Type_: List of <a href="applicationexceptiondefinition.md">ApplicationExceptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Decoder

_Required_: No

_Type_: List of <a href="decoderdefinition.md">DecoderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineLearningException

_Required_: No

_Type_: List of <a href="machinelearningexceptiondefinition.md">MachineLearningExceptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineLearningModel

_Required_: No

_Type_: List of <a href="machinelearningmodeldefinition.md">MachineLearningModelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

