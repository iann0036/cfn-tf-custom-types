# Terraform::Kubernetes::StatefulSet

Manages the deployment and scaling of a set of Pods , and provides guarantees about the 
ordering and uniqueness of these Pods.

Like a Deployment , a StatefulSet manages Pods that are based on an identical container spec.
Unlike a Deployment, a StatefulSet maintains a sticky identity for each of their Pods.
These pods are created from the same spec, but are not interchangeable: each has a persistent 
identifier that it maintains across any rescheduling.

A StatefulSet operates under the same pattern as any other Controller.
You define your desired state in a StatefulSet object, and the StatefulSet controller makes any 
necessary updates to get there from the current state.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::StatefulSet",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="spec.md">Spec</a>, ... ]</i>,
        "<a href="#selector" title="Selector">Selector</a>" : <i>[ <a href="selector.md">Selector</a>, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="template.md">Template</a>, ... ]</i>,
        "<a href="#updatestrategy" title="UpdateStrategy">UpdateStrategy</a>" : <i>[ <a href="updatestrategy.md">UpdateStrategy</a>, ... ]</i>,
        "<a href="#volumeclaimtemplate" title="VolumeClaimTemplate">VolumeClaimTemplate</a>" : <i>[ <a href="volumeclaimtemplate.md">VolumeClaimTemplate</a>, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressions.md">MatchExpressions</a>, ... ]</i>,
        "<a href="#rollingupdate" title="RollingUpdate">RollingUpdate</a>" : <i>[ <a href="rollingupdate.md">RollingUpdate</a>, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resources.md">Resources</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::StatefulSet
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="spec.md">Spec</a></i>
    <a href="#selector" title="Selector">Selector</a>: <i>
      - <a href="selector.md">Selector</a></i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="template.md">Template</a></i>
    <a href="#updatestrategy" title="UpdateStrategy">UpdateStrategy</a>: <i>
      - <a href="updatestrategy.md">UpdateStrategy</a></i>
    <a href="#volumeclaimtemplate" title="VolumeClaimTemplate">VolumeClaimTemplate</a>: <i>
      - <a href="volumeclaimtemplate.md">VolumeClaimTemplate</a></i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressions.md">MatchExpressions</a></i>
    <a href="#rollingupdate" title="RollingUpdate">RollingUpdate</a>: <i>
      - <a href="rollingupdate.md">RollingUpdate</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resources.md">Resources</a></i>
</pre>

## Properties

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="spec.md">Spec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of <a href="selector.md">Selector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="template.md">Template</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateStrategy

_Required_: No

_Type_: List of <a href="updatestrategy.md">UpdateStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeClaimTemplate

_Required_: No

_Type_: List of <a href="volumeclaimtemplate.md">VolumeClaimTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressions.md">MatchExpressions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingUpdate

_Required_: No

_Type_: List of <a href="rollingupdate.md">RollingUpdate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resources.md">Resources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

