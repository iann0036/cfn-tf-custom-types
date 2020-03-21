# Terraform::Kubernetes::Deployment Iscsi

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#iqn" title="Iqn">Iqn</a>" : <i>String</i>,
    "<a href="#iscsiinterface" title="IscsiInterface">IscsiInterface</a>" : <i>String</i>,
    "<a href="#lun" title="Lun">Lun</a>" : <i>Double</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#targetportal" title="TargetPortal">TargetPortal</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#iqn" title="Iqn">Iqn</a>: <i>String</i>
<a href="#iscsiinterface" title="IscsiInterface">IscsiInterface</a>: <i>String</i>
<a href="#lun" title="Lun">Lun</a>: <i>Double</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#targetportal" title="TargetPortal">TargetPortal</a>: <i>String</i>
</pre>

## Properties

#### FsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iqn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lun

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPortal

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

