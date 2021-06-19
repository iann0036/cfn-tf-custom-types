# TF::AWS::Wafv2WebAclAssociation

Creates a WAFv2 Web ACL Association.

~> **NOTE on associating a WAFv2 Web ACL with a Cloudfront distribution:** Do not use this resource to associate a WAFv2 Web ACL with a Cloudfront Distribution. The [AWS API call backing this resource][1] notes that you should use the [`web_acl_id`][2] property on the [`cloudfront_distribution`][2] instead.

[1]: https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html
[2]: /docs/providers/aws/r/cloudfront_distribution.html#web_acl_id

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Wafv2WebAclAssociation",
    "Properties" : {
        "<a href="#resourcearn" title="ResourceArn">ResourceArn</a>" : <i>String</i>,
        "<a href="#webaclarn" title="WebAclArn">WebAclArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Wafv2WebAclAssociation
Properties:
    <a href="#resourcearn" title="ResourceArn">ResourceArn</a>: <i>String</i>
    <a href="#webaclarn" title="WebAclArn">WebAclArn</a>: <i>String</i>
</pre>

## Properties

#### ResourceArn

The Amazon Resource Name (ARN) of the resource to associate with the web ACL. This must be an ARN of an Application Load Balancer or an Amazon API Gateway stage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAclArn

The Amazon Resource Name (ARN) of the Web ACL that you want to associate with the resource.

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

