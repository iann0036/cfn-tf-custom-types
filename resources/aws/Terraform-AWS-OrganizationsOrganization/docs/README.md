# Terraform::AWS::OrganizationsOrganization

Provides a resource to create an organization.

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
</pre>

## Properties

#### AwsServiceAccessPrincipals

List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledPolicyTypes

List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSet

Specify "ALL" (default) or "CONSOLIDATED_BILLING".

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

Returns the <code>Accounts</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### MasterAccountArn

Returns the <code>MasterAccountArn</code> value.

#### MasterAccountEmail

Returns the <code>MasterAccountEmail</code> value.

#### MasterAccountId

Returns the <code>MasterAccountId</code> value.

#### NonMasterAccounts

Returns the <code>NonMasterAccounts</code> value.

#### Roots

Returns the <code>Roots</code> value.

