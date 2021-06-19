# TF::Cloudtamerio::CloudRule

CloudFormation equivalent of cloudtamerio_cloud_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudtamerio::CloudRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#lastupdated" title="LastUpdated">LastUpdated</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#postwebhookid" title="PostWebhookId">PostWebhookId</a>" : <i>Double</i>,
        "<a href="#prewebhookid" title="PreWebhookId">PreWebhookId</a>" : <i>Double</i>,
        "<a href="#awscloudformationtemplates" title="AwsCloudformationTemplates">AwsCloudformationTemplates</a>" : <i>[ <a href="awscloudformationtemplatesdefinition.md">AwsCloudformationTemplatesDefinition</a>, ... ]</i>,
        "<a href="#awsiampolicies" title="AwsIamPolicies">AwsIamPolicies</a>" : <i>[ <a href="awsiampoliciesdefinition.md">AwsIamPoliciesDefinition</a>, ... ]</i>,
        "<a href="#azurearmtemplatedefinitions" title="AzureArmTemplateDefinitions">AzureArmTemplateDefinitions</a>" : <i>[ <a href="azurearmtemplatedefinitionsdefinition.md">AzureArmTemplateDefinitionsDefinition</a>, ... ]</i>,
        "<a href="#azurepolicydefinitions" title="AzurePolicyDefinitions">AzurePolicyDefinitions</a>" : <i>[ <a href="azurepolicydefinitionsdefinition.md">AzurePolicyDefinitionsDefinition</a>, ... ]</i>,
        "<a href="#azureroledefinitions" title="AzureRoleDefinitions">AzureRoleDefinitions</a>" : <i>[ <a href="azureroledefinitionsdefinition.md">AzureRoleDefinitionsDefinition</a>, ... ]</i>,
        "<a href="#compliancestandards" title="ComplianceStandards">ComplianceStandards</a>" : <i>[ <a href="compliancestandardsdefinition.md">ComplianceStandardsDefinition</a>, ... ]</i>,
        "<a href="#internalawsamis" title="InternalAwsAmis">InternalAwsAmis</a>" : <i>[ <a href="internalawsamisdefinition.md">InternalAwsAmisDefinition</a>, ... ]</i>,
        "<a href="#internalawsservicecatalogportfolios" title="InternalAwsServiceCatalogPortfolios">InternalAwsServiceCatalogPortfolios</a>" : <i>[ <a href="internalawsservicecatalogportfoliosdefinition.md">InternalAwsServiceCatalogPortfoliosDefinition</a>, ... ]</i>,
        "<a href="#ous" title="Ous">Ous</a>" : <i>[ <a href="ousdefinition.md">OusDefinition</a>, ... ]</i>,
        "<a href="#ownerusergroups" title="OwnerUserGroups">OwnerUserGroups</a>" : <i>[ <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a>, ... ]</i>,
        "<a href="#ownerusers" title="OwnerUsers">OwnerUsers</a>" : <i>[ <a href="ownerusersdefinition.md">OwnerUsersDefinition</a>, ... ]</i>,
        "<a href="#projects" title="Projects">Projects</a>" : <i>[ <a href="projectsdefinition.md">ProjectsDefinition</a>, ... ]</i>,
        "<a href="#servicecontrolpolicies" title="ServiceControlPolicies">ServiceControlPolicies</a>" : <i>[ <a href="servicecontrolpoliciesdefinition.md">ServiceControlPoliciesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudtamerio::CloudRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#lastupdated" title="LastUpdated">LastUpdated</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#postwebhookid" title="PostWebhookId">PostWebhookId</a>: <i>Double</i>
    <a href="#prewebhookid" title="PreWebhookId">PreWebhookId</a>: <i>Double</i>
    <a href="#awscloudformationtemplates" title="AwsCloudformationTemplates">AwsCloudformationTemplates</a>: <i>
      - <a href="awscloudformationtemplatesdefinition.md">AwsCloudformationTemplatesDefinition</a></i>
    <a href="#awsiampolicies" title="AwsIamPolicies">AwsIamPolicies</a>: <i>
      - <a href="awsiampoliciesdefinition.md">AwsIamPoliciesDefinition</a></i>
    <a href="#azurearmtemplatedefinitions" title="AzureArmTemplateDefinitions">AzureArmTemplateDefinitions</a>: <i>
      - <a href="azurearmtemplatedefinitionsdefinition.md">AzureArmTemplateDefinitionsDefinition</a></i>
    <a href="#azurepolicydefinitions" title="AzurePolicyDefinitions">AzurePolicyDefinitions</a>: <i>
      - <a href="azurepolicydefinitionsdefinition.md">AzurePolicyDefinitionsDefinition</a></i>
    <a href="#azureroledefinitions" title="AzureRoleDefinitions">AzureRoleDefinitions</a>: <i>
      - <a href="azureroledefinitionsdefinition.md">AzureRoleDefinitionsDefinition</a></i>
    <a href="#compliancestandards" title="ComplianceStandards">ComplianceStandards</a>: <i>
      - <a href="compliancestandardsdefinition.md">ComplianceStandardsDefinition</a></i>
    <a href="#internalawsamis" title="InternalAwsAmis">InternalAwsAmis</a>: <i>
      - <a href="internalawsamisdefinition.md">InternalAwsAmisDefinition</a></i>
    <a href="#internalawsservicecatalogportfolios" title="InternalAwsServiceCatalogPortfolios">InternalAwsServiceCatalogPortfolios</a>: <i>
      - <a href="internalawsservicecatalogportfoliosdefinition.md">InternalAwsServiceCatalogPortfoliosDefinition</a></i>
    <a href="#ous" title="Ous">Ous</a>: <i>
      - <a href="ousdefinition.md">OusDefinition</a></i>
    <a href="#ownerusergroups" title="OwnerUserGroups">OwnerUserGroups</a>: <i>
      - <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a></i>
    <a href="#ownerusers" title="OwnerUsers">OwnerUsers</a>: <i>
      - <a href="ownerusersdefinition.md">OwnerUsersDefinition</a></i>
    <a href="#projects" title="Projects">Projects</a>: <i>
      - <a href="projectsdefinition.md">ProjectsDefinition</a></i>
    <a href="#servicecontrolpolicies" title="ServiceControlPolicies">ServiceControlPolicies</a>: <i>
      - <a href="servicecontrolpoliciesdefinition.md">ServiceControlPoliciesDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostWebhookId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreWebhookId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCloudformationTemplates

_Required_: No

_Type_: List of <a href="awscloudformationtemplatesdefinition.md">AwsCloudformationTemplatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsIamPolicies

_Required_: No

_Type_: List of <a href="awsiampoliciesdefinition.md">AwsIamPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureArmTemplateDefinitions

_Required_: No

_Type_: List of <a href="azurearmtemplatedefinitionsdefinition.md">AzureArmTemplateDefinitionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurePolicyDefinitions

_Required_: No

_Type_: List of <a href="azurepolicydefinitionsdefinition.md">AzurePolicyDefinitionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureRoleDefinitions

_Required_: No

_Type_: List of <a href="azureroledefinitionsdefinition.md">AzureRoleDefinitionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceStandards

_Required_: No

_Type_: List of <a href="compliancestandardsdefinition.md">ComplianceStandardsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalAwsAmis

_Required_: No

_Type_: List of <a href="internalawsamisdefinition.md">InternalAwsAmisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalAwsServiceCatalogPortfolios

_Required_: No

_Type_: List of <a href="internalawsservicecatalogportfoliosdefinition.md">InternalAwsServiceCatalogPortfoliosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ous

_Required_: No

_Type_: List of <a href="ousdefinition.md">OusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerUserGroups

_Required_: No

_Type_: List of <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerUsers

_Required_: No

_Type_: List of <a href="ownerusersdefinition.md">OwnerUsersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Projects

_Required_: No

_Type_: List of <a href="projectsdefinition.md">ProjectsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceControlPolicies

_Required_: No

_Type_: List of <a href="servicecontrolpoliciesdefinition.md">ServiceControlPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BuiltIn

Returns the <code>BuiltIn</code> value.

#### Id

Returns the <code>Id</code> value.

