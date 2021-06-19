# TF::Kubernetes::CronJob ValueFromDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>" : <i>[ <a href="configmapkeyrefdefinition.md">ConfigMapKeyRefDefinition</a>, ... ]</i>,
    "<a href="#fieldref" title="FieldRef">FieldRef</a>" : <i>[ <a href="fieldrefdefinition.md">FieldRefDefinition</a>, ... ]</i>,
    "<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>" : <i>[ <a href="resourcefieldrefdefinition.md">ResourceFieldRefDefinition</a>, ... ]</i>,
    "<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>" : <i>[ <a href="secretkeyrefdefinition.md">SecretKeyRefDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>: <i>
      - <a href="configmapkeyrefdefinition.md">ConfigMapKeyRefDefinition</a></i>
<a href="#fieldref" title="FieldRef">FieldRef</a>: <i>
      - <a href="fieldrefdefinition.md">FieldRefDefinition</a></i>
<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>: <i>
      - <a href="resourcefieldrefdefinition.md">ResourceFieldRefDefinition</a></i>
<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>: <i>
      - <a href="secretkeyrefdefinition.md">SecretKeyRefDefinition</a></i>
</pre>

## Properties

#### ConfigMapKeyRef

_Required_: No

_Type_: List of <a href="configmapkeyrefdefinition.md">ConfigMapKeyRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldRef

_Required_: No

_Type_: List of <a href="fieldrefdefinition.md">FieldRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFieldRef

_Required_: No

_Type_: List of <a href="resourcefieldrefdefinition.md">ResourceFieldRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKeyRef

_Required_: No

_Type_: List of <a href="secretkeyrefdefinition.md">SecretKeyRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

