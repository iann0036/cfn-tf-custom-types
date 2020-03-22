# Terraform::AzureStack::TemplateDeployment

Manages a template deployment of resources

~> **Note on ARM Template Deployments:** Due to the way the underlying Azure API is designed, Terraform can only manage the deployment of the ARM Template - and not any resources which are created by it.
This means that when deleting the `azurestack_template_deployment` resource, Terraform will only remove the reference to the deployment, whilst leaving any resources created by that ARM Template Deployment.
One workaround for this is to use a unique Resource Group for each ARM Template Deployment, which means deleting the Resource Group would contain any resources created within it - however this isn't ideal. [More information](https://docs.microsoft.com/en-us/rest/api/resources/deployments#Deployments_Delete).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::TemplateDeployment",
    "Properties" : {
        "<a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#parametersbody" title="ParametersBody">ParametersBody</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#templatebody" title="TemplateBody">TemplateBody</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::TemplateDeployment
Properties:
    <a href="#deploymentmode" title="DeploymentMode">DeploymentMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#parametersbody" title="ParametersBody">ParametersBody</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#templatebody" title="TemplateBody">TemplateBody</a>: <i>String</i>
</pre>

## Properties

#### DeploymentMode

Specifies the mode that is used to deploy resources. This value could be either `Incremental` or `Complete`.
Note that you will almost *always* want this to be set to `Incremental` otherwise the deployment will destroy all infrastructure not
specified within the template, and Terraform will not be aware of this.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the template deployment. Changing this forces a
new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

Specifies the name and value pairs that define the deployment parameters for the template.

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParametersBody

Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the template deployment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateBody

Specifies the JSON definition for the template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Outputs

Returns the <code>Outputs</code> value.

