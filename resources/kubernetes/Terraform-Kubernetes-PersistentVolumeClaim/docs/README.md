# Terraform::Kubernetes::PersistentVolumeClaim

This resource allows the user to request for and claim to a persistent volume.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::PersistentVolumeClaim",
    "Properties" : {
        "<a href="#waituntilbound" title="WaitUntilBound">WaitUntilBound</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="spec.md">Spec</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resources.md">Resources</a>, ... ]</i>,
        "<a href="#selector" title="Selector">Selector</a>" : <i>[ <a href="selector.md">Selector</a>, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressions.md">MatchExpressions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::PersistentVolumeClaim
Properties:
    <a href="#waituntilbound" title="WaitUntilBound">WaitUntilBound</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="spec.md">Spec</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resources.md">Resources</a></i>
    <a href="#selector" title="Selector">Selector</a>: <i>
      - <a href="selector.md">Selector</a></i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressions.md">MatchExpressions</a></i>
</pre>

## Properties

#### WaitUntilBound

Whether to wait for the claim to reach `Bound` state (to find volume in which to claim the space).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="spec.md">Spec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resources.md">Resources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of <a href="selector.md">Selector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressions.md">MatchExpressions</a>

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

