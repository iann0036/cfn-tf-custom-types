# TF::AWS::CodeartifactRepositoryPermissionsPolicy

Provides a CodeArtifact Repostory Permissions Policy Resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CodeartifactRepositoryPermissionsPolicy",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#domainowner" title="DomainOwner">DomainOwner</a>" : <i>String</i>,
        "<a href="#policydocument" title="PolicyDocument">PolicyDocument</a>" : <i>String</i>,
        "<a href="#policyrevision" title="PolicyRevision">PolicyRevision</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CodeartifactRepositoryPermissionsPolicy
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#domainowner" title="DomainOwner">DomainOwner</a>: <i>String</i>
    <a href="#policydocument" title="PolicyDocument">PolicyDocument</a>: <i>String</i>
    <a href="#policyrevision" title="PolicyRevision">PolicyRevision</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
</pre>

## Properties

#### Domain

The name of the domain on which to set the resource policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainOwner

The account number of the AWS account that owns the domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDocument

A JSON policy string to be set as the access control resource policy on the provided domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyRevision

The current revision of the resource policy to be set. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The name of the repository to set the resource policy on.

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

#### ResourceArn

Returns the <code>ResourceArn</code> value.

