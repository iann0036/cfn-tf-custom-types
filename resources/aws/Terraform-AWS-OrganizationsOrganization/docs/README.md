# Terraform::AWS::OrganizationsOrganization

CloudFormation equivalent of aws_organizations_organization

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OrganizationsOrganization",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accounts" title="Accounts">Accounts</a>" : <i>[ &lt;a href=&#34;accounts.md&#34;&gt;Accounts&lt;/a&gt;, ... ]</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#awsserviceaccessprincipals" title="AwsServiceAccessPrincipals">AwsServiceAccessPrincipals</a>" : <i>[ String, ... ]</i>,
        "<a href="#enabledpolicytypes" title="EnabledPolicyTypes">EnabledPolicyTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#featureset" title="FeatureSet">FeatureSet</a>" : <i>String</i>,
        "<a href="#masteraccountarn" title="MasterAccountArn">MasterAccountArn</a>" : <i>String</i>,
        "<a href="#masteraccountemail" title="MasterAccountEmail">MasterAccountEmail</a>" : <i>String</i>,
        "<a href="#masteraccountid" title="MasterAccountId">MasterAccountId</a>" : <i>String</i>,
        "<a href="#nonmasteraccounts" title="NonMasterAccounts">NonMasterAccounts</a>" : <i>[ &lt;a href=&#34;nonmasteraccounts.md&#34;&gt;NonMasterAccounts&lt;/a&gt;, ... ]</i>,
        "<a href="#roots" title="Roots">Roots</a>" : <i>[ &lt;a href=&#34;roots.md&#34;&gt;Roots&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OrganizationsOrganization
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accounts" title="Accounts">Accounts</a>: <i>
      - &lt;a href=&#34;accounts.md&#34;&gt;Accounts&lt;/a&gt;</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#awsserviceaccessprincipals" title="AwsServiceAccessPrincipals">AwsServiceAccessPrincipals</a>: <i>
      - String</i>
    <a href="#enabledpolicytypes" title="EnabledPolicyTypes">EnabledPolicyTypes</a>: <i>
      - String</i>
    <a href="#featureset" title="FeatureSet">FeatureSet</a>: <i>String</i>
    <a href="#masteraccountarn" title="MasterAccountArn">MasterAccountArn</a>: <i>String</i>
    <a href="#masteraccountemail" title="MasterAccountEmail">MasterAccountEmail</a>: <i>String</i>
    <a href="#masteraccountid" title="MasterAccountId">MasterAccountId</a>: <i>String</i>
    <a href="#nonmasteraccounts" title="NonMasterAccounts">NonMasterAccounts</a>: <i>
      - &lt;a href=&#34;nonmasteraccounts.md&#34;&gt;NonMasterAccounts&lt;/a&gt;</i>
    <a href="#roots" title="Roots">Roots</a>: <i>
      - &lt;a href=&#34;roots.md&#34;&gt;Roots&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accounts

_Required_: No

_Type_: List of &lt;a href=&#34;accounts.md&#34;&gt;Accounts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### MasterAccountArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAccountEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonMasterAccounts

_Required_: No

_Type_: List of &lt;a href=&#34;nonmasteraccounts.md&#34;&gt;NonMasterAccounts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roots

_Required_: No

_Type_: List of &lt;a href=&#34;roots.md&#34;&gt;Roots&lt;/a&gt;

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

