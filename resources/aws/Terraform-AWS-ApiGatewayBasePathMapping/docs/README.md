# Terraform::AWS::ApiGatewayBasePathMapping

Connects a custom domain name registered via `aws_api_gateway_domain_name`
with a deployed API so that its methods can be called via the
custom domain name.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayBasePathMapping",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#basepath" title="BasePath">BasePath</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#stagename" title="StageName">StageName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayBasePathMapping
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#basepath" title="BasePath">BasePath</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#stagename" title="StageName">StageName</a>: <i>String</i>
</pre>

## Properties

#### ApiId

The id of the API to connect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasePath

Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

The already-registered domain name to connect the API to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageName

The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

_Required_: No

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

