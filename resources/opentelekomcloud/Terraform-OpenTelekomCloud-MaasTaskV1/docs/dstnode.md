# Terraform::OpenTelekomCloud::MaasTaskV1 DstNode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ak" title="Ak">Ak</a>" : <i>String</i>,
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#objectkey" title="ObjectKey">ObjectKey</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#sk" title="Sk">Sk</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ak" title="Ak">Ak</a>: <i>String</i>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#objectkey" title="ObjectKey">ObjectKey</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#sk" title="Sk">Sk</a>: <i>String</i>
</pre>

## Properties

#### Ak

Specifies the destination bucket Access Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

Specifies the name of the destination bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectKey

Specifies the name of the object to be selected in the
destination bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sk

Specifies the destination bucket Secret Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

