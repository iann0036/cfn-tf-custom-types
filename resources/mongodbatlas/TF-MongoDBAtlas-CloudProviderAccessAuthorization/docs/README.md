# TF::MongoDBAtlas::CloudProviderAccessAuthorization

CloudFormation equivalent of mongodbatlas_cloud_provider_access_authorization

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::CloudProviderAccessAuthorization",
    "Properties" : {
        "<a href="#aws" title="Aws">Aws</a>" : <i>[ <a href="awsdefinition.md">AwsDefinition</a>, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#roleid" title="RoleId">RoleId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::CloudProviderAccessAuthorization
Properties:
    <a href="#aws" title="Aws">Aws</a>: <i>
      - <a href="awsdefinition.md">AwsDefinition</a></i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#roleid" title="RoleId">RoleId</a>: <i>String</i>
</pre>

## Properties

#### Aws

_Required_: No

_Type_: List of <a href="awsdefinition.md">AwsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleId

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

#### AuthorizedDate

Returns the <code>AuthorizedDate</code> value.

#### FeatureUsages

Returns the <code>FeatureUsages</code> value.

#### Id

Returns the <code>Id</code> value.

