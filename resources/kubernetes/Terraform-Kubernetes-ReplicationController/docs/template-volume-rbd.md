# Terraform::Kubernetes::ReplicationController Template Volume Rbd

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cephmonitors" title="CephMonitors">CephMonitors</a>" : <i>[ String, ... ]</i>,
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#keyring" title="Keyring">Keyring</a>" : <i>String</i>,
    "<a href="#radosuser" title="RadosUser">RadosUser</a>" : <i>String</i>,
    "<a href="#rbdimage" title="RbdImage">RbdImage</a>" : <i>String</i>,
    "<a href="#rbdpool" title="RbdPool">RbdPool</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ <a href="template-volume-rbd-secretref.md">SecretRef</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cephmonitors" title="CephMonitors">CephMonitors</a>: <i>
      - String</i>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#keyring" title="Keyring">Keyring</a>: <i>String</i>
<a href="#radosuser" title="RadosUser">RadosUser</a>: <i>String</i>
<a href="#rbdimage" title="RbdImage">RbdImage</a>: <i>String</i>
<a href="#rbdpool" title="RbdPool">RbdPool</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - <a href="template-volume-rbd-secretref.md">SecretRef</a></i>
</pre>

## Properties

#### CephMonitors

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keyring

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadosUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RbdImage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RbdPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of <a href="template-volume-rbd-secretref.md">SecretRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

