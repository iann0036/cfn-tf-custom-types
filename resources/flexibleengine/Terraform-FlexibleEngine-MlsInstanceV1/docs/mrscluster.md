# Terraform::FlexibleEngine::MlsInstanceV1 MrsCluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
    "<a href="#userpassword" title="UserPassword">UserPassword</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#username" title="UserName">UserName</a>: <i>String</i>
<a href="#userpassword" title="UserPassword">UserPassword</a>: <i>String</i>
</pre>

## Properties

#### Id

Specifies the ID of the MRS cluster. Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

Specifies the MRS cluster username. This parameter is mandatory
only when the MRS cluster is in the security mode. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPassword

Specifies the password of the MRS cluster user. The password
and username work in a pair. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

