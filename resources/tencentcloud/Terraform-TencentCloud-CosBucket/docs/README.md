# Terraform::TencentCloud::CosBucket

Provides a COS resource to create a COS bucket and set its attributes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::CosBucket",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#corsrules" title="CorsRules">CorsRules</a>" : <i>[ <a href="corsrules.md">CorsRules</a>, ... ]</i>,
        "<a href="#lifecyclerules" title="LifecycleRules">LifecycleRules</a>" : <i>[ <a href="lifecyclerules.md">LifecycleRules</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="website.md">Website</a>, ... ]</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expiration.md">Expiration</a>, ... ]</i>,
        "<a href="#transition" title="Transition">Transition</a>" : <i>[ <a href="transition.md">Transition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::CosBucket
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#corsrules" title="CorsRules">CorsRules</a>: <i>
      - <a href="corsrules.md">CorsRules</a></i>
    <a href="#lifecyclerules" title="LifecycleRules">LifecycleRules</a>: <i>
      - <a href="lifecyclerules.md">LifecycleRules</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="website.md">Website</a></i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expiration.md">Expiration</a></i>
    <a href="#transition" title="Transition">Transition</a>: <i>
      - <a href="transition.md">Transition</a></i>
</pre>

## Properties

#### Acl

The canned ACL to apply. Available values include private, public-read, and public-read-write. Defaults to private.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of a bucket to be created. Bucket format should be [custom name]-[appid], for example `mycos-1258798060`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of a bucket.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRules

_Required_: No

_Type_: List of <a href="corsrules.md">CorsRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRules

_Required_: No

_Type_: List of <a href="lifecyclerules.md">LifecycleRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of <a href="website.md">Website</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expiration.md">Expiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No

_Type_: List of <a href="transition.md">Transition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

