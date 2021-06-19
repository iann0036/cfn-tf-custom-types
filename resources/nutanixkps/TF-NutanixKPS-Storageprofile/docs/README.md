# TF::NutanixKPS::Storageprofile

CloudFormation equivalent of nutanixkps_storageprofile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NutanixKPS::Storageprofile",
    "Properties" : {
        "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicedomainid" title="ServiceDomainId">ServiceDomainId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#ebsstorageconfig" title="EbsStorageConfig">EbsStorageConfig</a>" : <i>[ <a href="ebsstorageconfigdefinition.md">EbsStorageConfigDefinition</a>, ... ]</i>,
        "<a href="#nutanixvolumesconfig" title="NutanixVolumesConfig">NutanixVolumesConfig</a>" : <i>[ <a href="nutanixvolumesconfigdefinition.md">NutanixVolumesConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NutanixKPS::Storageprofile
Properties:
    <a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicedomainid" title="ServiceDomainId">ServiceDomainId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#ebsstorageconfig" title="EbsStorageConfig">EbsStorageConfig</a>: <i>
      - <a href="ebsstorageconfigdefinition.md">EbsStorageConfigDefinition</a></i>
    <a href="#nutanixvolumesconfig" title="NutanixVolumesConfig">NutanixVolumesConfig</a>: <i>
      - <a href="nutanixvolumesconfigdefinition.md">NutanixVolumesConfigDefinition</a></i>
</pre>

## Properties

#### IsDefault

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDomainId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsStorageConfig

_Required_: No

_Type_: List of <a href="ebsstorageconfigdefinition.md">EbsStorageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NutanixVolumesConfig

_Required_: No

_Type_: List of <a href="nutanixvolumesconfigdefinition.md">NutanixVolumesConfigDefinition</a>

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

