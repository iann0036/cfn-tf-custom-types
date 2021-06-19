# TF::AzureRM::HealthcareService AuthenticationConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#audience" title="Audience">Audience</a>" : <i>String</i>,
    "<a href="#authority" title="Authority">Authority</a>" : <i>String</i>,
    "<a href="#smartproxyenabled" title="SmartProxyEnabled">SmartProxyEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#audience" title="Audience">Audience</a>: <i>String</i>
<a href="#authority" title="Authority">Authority</a>: <i>String</i>
<a href="#smartproxyenabled" title="SmartProxyEnabled">SmartProxyEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Audience

The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authority

The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running Terraform.
Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmartProxyEnabled

Enables the 'SMART on FHIR' option for mobile and web implementations.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

