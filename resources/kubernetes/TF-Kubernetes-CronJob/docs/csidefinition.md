# TF::Kubernetes::CronJob CsiDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#volumeattributes" title="VolumeAttributes">VolumeAttributes</a>" : <i>[ <a href="volumeattributesdefinition.md">VolumeAttributesDefinition</a>, ... ]</i>,
    "<a href="#volumehandle" title="VolumeHandle">VolumeHandle</a>" : <i>String</i>,
    "<a href="#controllerexpandsecretref" title="ControllerExpandSecretRef">ControllerExpandSecretRef</a>" : <i>[ <a href="controllerexpandsecretrefdefinition.md">ControllerExpandSecretRefDefinition</a>, ... ]</i>,
    "<a href="#controllerpublishsecretref" title="ControllerPublishSecretRef">ControllerPublishSecretRef</a>" : <i>[ <a href="controllerpublishsecretrefdefinition.md">ControllerPublishSecretRefDefinition</a>, ... ]</i>,
    "<a href="#nodepublishsecretref" title="NodePublishSecretRef">NodePublishSecretRef</a>" : <i>[ <a href="nodepublishsecretrefdefinition.md">NodePublishSecretRefDefinition</a>, ... ]</i>,
    "<a href="#nodestagesecretref" title="NodeStageSecretRef">NodeStageSecretRef</a>" : <i>[ <a href="nodestagesecretrefdefinition.md">NodeStageSecretRefDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#volumeattributes" title="VolumeAttributes">VolumeAttributes</a>: <i>
      - <a href="volumeattributesdefinition.md">VolumeAttributesDefinition</a></i>
<a href="#volumehandle" title="VolumeHandle">VolumeHandle</a>: <i>String</i>
<a href="#controllerexpandsecretref" title="ControllerExpandSecretRef">ControllerExpandSecretRef</a>: <i>
      - <a href="controllerexpandsecretrefdefinition.md">ControllerExpandSecretRefDefinition</a></i>
<a href="#controllerpublishsecretref" title="ControllerPublishSecretRef">ControllerPublishSecretRef</a>: <i>
      - <a href="controllerpublishsecretrefdefinition.md">ControllerPublishSecretRefDefinition</a></i>
<a href="#nodepublishsecretref" title="NodePublishSecretRef">NodePublishSecretRef</a>: <i>
      - <a href="nodepublishsecretrefdefinition.md">NodePublishSecretRefDefinition</a></i>
<a href="#nodestagesecretref" title="NodeStageSecretRef">NodeStageSecretRef</a>: <i>
      - <a href="nodestagesecretrefdefinition.md">NodeStageSecretRefDefinition</a></i>
</pre>

## Properties

#### Driver

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeAttributes

_Required_: No

_Type_: List of <a href="volumeattributesdefinition.md">VolumeAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeHandle

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerExpandSecretRef

_Required_: No

_Type_: List of <a href="controllerexpandsecretrefdefinition.md">ControllerExpandSecretRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerPublishSecretRef

_Required_: No

_Type_: List of <a href="controllerpublishsecretrefdefinition.md">ControllerPublishSecretRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePublishSecretRef

_Required_: No

_Type_: List of <a href="nodepublishsecretrefdefinition.md">NodePublishSecretRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeStageSecretRef

_Required_: No

_Type_: List of <a href="nodestagesecretrefdefinition.md">NodeStageSecretRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

