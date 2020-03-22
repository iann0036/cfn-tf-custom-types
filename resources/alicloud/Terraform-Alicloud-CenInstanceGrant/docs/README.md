# Terraform::Alicloud::CenInstanceGrant

Provides a CEN child instance grant resource, which allow you to authorize a VPC or VBR to a CEN of a different account.

For more information about how to use it, see [Attach a network in a different account](https://www.alibabacloud.com/help/doc-detail/73645.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CenInstanceGrant",
    "Properties" : {
        "<a href="#cenid" title="CenId">CenId</a>" : <i>String</i>,
        "<a href="#cenownerid" title="CenOwnerId">CenOwnerId</a>" : <i>String</i>,
        "<a href="#childinstanceid" title="ChildInstanceId">ChildInstanceId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CenInstanceGrant
Properties:
    <a href="#cenid" title="CenId">CenId</a>: <i>String</i>
    <a href="#cenownerid" title="CenOwnerId">CenOwnerId</a>: <i>String</i>
    <a href="#childinstanceid" title="ChildInstanceId">ChildInstanceId</a>: <i>String</i>
</pre>

## Properties

#### CenId

The ID of the CEN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CenOwnerId

The owner UID of the  CEN which the child instance granted to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildInstanceId

The ID of the child instance to grant.

_Required_: Yes

_Type_: String

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

