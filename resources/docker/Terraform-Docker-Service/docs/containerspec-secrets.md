# Terraform::Docker::Service ContainerSpec Secrets

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filegid" title="FileGid">FileGid</a>" : <i>String</i>,
    "<a href="#filemode" title="FileMode">FileMode</a>" : <i>Double</i>,
    "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
    "<a href="#fileuid" title="FileUid">FileUid</a>" : <i>String</i>,
    "<a href="#secretid" title="SecretId">SecretId</a>" : <i>String</i>,
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filegid" title="FileGid">FileGid</a>: <i>String</i>
<a href="#filemode" title="FileMode">FileMode</a>: <i>Double</i>
<a href="#filename" title="FileName">FileName</a>: <i>String</i>
<a href="#fileuid" title="FileUid">FileUid</a>: <i>String</i>
<a href="#secretid" title="SecretId">SecretId</a>: <i>String</i>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
</pre>

## Properties

#### FileGid

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileMode

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUid

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

