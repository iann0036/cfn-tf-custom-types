# Terraform::OpenTelekomCloud::MaasTaskV1 SrcNode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ak" title="Ak">Ak</a>" : <i>String</i>,
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>String</i>,
    "<a href="#objectkey" title="ObjectKey">ObjectKey</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#sk" title="Sk">Sk</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ak" title="Ak">Ak</a>: <i>String</i>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#cloudtype" title="CloudType">CloudType</a>: <i>String</i>
<a href="#objectkey" title="ObjectKey">ObjectKey</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#sk" title="Sk">Sk</a>: <i>String</i>
</pre>

## Properties

#### Ak

Specifies the source bucket Access Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

Specifies the name of the source bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

Specifies the source cloud vendor. The default value is
AWS and only AWS is supported now.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectKey

Specifies the name of the object to be selected in the
source bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sk

Specifies the source bucket Secret Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

