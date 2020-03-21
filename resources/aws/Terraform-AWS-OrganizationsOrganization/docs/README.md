# Terraform::AWS::OrganizationsOrganization

CloudFormation equivalent of aws_organizations_organization

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OrganizationsOrganization",
    "Properties" : {
        "<a href="#awsserviceaccessprincipals" title="AwsServiceAccessPrincipals">AwsServiceAccessPrincipals</a>" : <i>[ String, ... ]</i>,
        "<a href="#enabledpolicytypes" title="EnabledPolicyTypes">EnabledPolicyTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#featureset" title="FeatureSet">FeatureSet</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OrganizationsOrganization
Properties:
    <a href="#awsserviceaccessprincipals" title="AwsServiceAccessPrincipals">AwsServiceAccessPrincipals</a>: <i>
      - String</i>
    <a href="#enabledpolicytypes" title="EnabledPolicyTypes">EnabledPolicyTypes</a>: <i>
      - String</i>
    <a href="#featureset" title="FeatureSet">FeatureSet</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
</pre>

## Properties

#### AwsServiceAccessPrincipals

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledPolicyTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

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

#### Accounts

Returns the &lt;code&gt;Accounts&lt;/code&gt; value.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### MasterAccountArn

Returns the &lt;code&gt;MasterAccountArn&lt;/code&gt; value.

#### MasterAccountEmail

Returns the &lt;code&gt;MasterAccountEmail&lt;/code&gt; value.

#### MasterAccountId

Returns the &lt;code&gt;MasterAccountId&lt;/code&gt; value.

#### NonMasterAccounts

Returns the &lt;code&gt;NonMasterAccounts&lt;/code&gt; value.

#### Roots

Returns the &lt;code&gt;Roots&lt;/code&gt; value.

