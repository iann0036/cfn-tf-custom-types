# Terraform::OCI::ObjectstorageObjectLifecyclePolicy

This resource provides the Object Lifecycle Policy resource in Oracle Cloud Infrastructure Object Storage service.

Creates or replaces the object lifecycle policy for the bucket.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::ObjectstorageObjectLifecyclePolicy",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rules.md">Rules</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#objectnamefilter" title="ObjectNameFilter">ObjectNameFilter</a>" : <i>[ <a href="objectnamefilter.md">ObjectNameFilter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::ObjectstorageObjectLifecyclePolicy
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rules.md">Rules</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#objectnamefilter" title="ObjectNameFilter">ObjectNameFilter</a>: <i>
      - <a href="objectnamefilter.md">ObjectNameFilter</a></i>
</pre>

## Properties

#### Bucket

The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The Object Storage namespace used for the request.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rules.md">Rules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectNameFilter

_Required_: No

_Type_: List of <a href="objectnamefilter.md">ObjectNameFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

