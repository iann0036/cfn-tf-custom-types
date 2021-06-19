# TF::UpCloud::Server LoginDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#createpassword" title="CreatePassword">CreatePassword</a>" : <i>Boolean</i>,
    "<a href="#keys" title="Keys">Keys</a>" : <i>[ String, ... ]</i>,
    "<a href="#passworddelivery" title="PasswordDelivery">PasswordDelivery</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#createpassword" title="CreatePassword">CreatePassword</a>: <i>Boolean</i>
<a href="#keys" title="Keys">Keys</a>: <i>
      - String</i>
<a href="#passworddelivery" title="PasswordDelivery">PasswordDelivery</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### CreatePassword

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordDelivery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

