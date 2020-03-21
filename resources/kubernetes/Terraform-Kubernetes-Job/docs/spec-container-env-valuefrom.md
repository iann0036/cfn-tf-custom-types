# Terraform::Kubernetes::Job Spec Container Env ValueFrom

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>" : <i>[ <a href="spec-container-env-valuefrom-configmapkeyref.md">ConfigMapKeyRef</a>, ... ]</i>,
    "<a href="#fieldref" title="FieldRef">FieldRef</a>" : <i>[ <a href="spec-container-env-valuefrom-fieldref.md">FieldRef</a>, ... ]</i>,
    "<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>" : <i>[ <a href="spec-container-env-valuefrom-resourcefieldref.md">ResourceFieldRef</a>, ... ]</i>,
    "<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>" : <i>[ <a href="spec-container-env-valuefrom-secretkeyref.md">SecretKeyRef</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>: <i>
      - <a href="spec-container-env-valuefrom-configmapkeyref.md">ConfigMapKeyRef</a></i>
<a href="#fieldref" title="FieldRef">FieldRef</a>: <i>
      - <a href="spec-container-env-valuefrom-fieldref.md">FieldRef</a></i>
<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>: <i>
      - <a href="spec-container-env-valuefrom-resourcefieldref.md">ResourceFieldRef</a></i>
<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>: <i>
      - <a href="spec-container-env-valuefrom-secretkeyref.md">SecretKeyRef</a></i>
</pre>

## Properties

#### ConfigMapKeyRef

_Required_: No

_Type_: List of <a href="spec-container-env-valuefrom-configmapkeyref.md">ConfigMapKeyRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldRef

_Required_: No

_Type_: List of <a href="spec-container-env-valuefrom-fieldref.md">FieldRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFieldRef

_Required_: No

_Type_: List of <a href="spec-container-env-valuefrom-resourcefieldref.md">ResourceFieldRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKeyRef

_Required_: No

_Type_: List of <a href="spec-container-env-valuefrom-secretkeyref.md">SecretKeyRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

