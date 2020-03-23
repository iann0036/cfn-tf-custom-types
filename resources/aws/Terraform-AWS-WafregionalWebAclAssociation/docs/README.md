# Terraform::AWS::WafregionalWebAclAssociation

Manages an association with WAF Regional Web ACL.

-> **Note:** An Application Load Balancer can only be associated with one WAF Regional WebACL.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::WafregionalWebAclAssociation",
    "Properties" : {
        "<a href="#resourcearn" title="ResourceArn">ResourceArn</a>" : <i>String</i>,
        "<a href="#webaclid" title="WebAclId">WebAclId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::WafregionalWebAclAssociation
Properties:
    <a href="#resourcearn" title="ResourceArn">ResourceArn</a>: <i>String</i>
    <a href="#webaclid" title="WebAclId">WebAclId</a>: <i>String</i>
</pre>

## Properties

#### ResourceArn

ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAclId

The ID of the WAF Regional WebACL to create an association.

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

