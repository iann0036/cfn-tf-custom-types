# Terraform::AzureRM::DataFactoryIntegrationRuntimeManaged CustomSetupScript

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blobcontaineruri" title="BlobContainerUri">BlobContainerUri</a>" : <i>String</i>,
    "<a href="#sastoken" title="SasToken">SasToken</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#blobcontaineruri" title="BlobContainerUri">BlobContainerUri</a>: <i>String</i>
<a href="#sastoken" title="SasToken">SasToken</a>: <i>String</i>
</pre>

## Properties

#### BlobContainerUri

The blob endpoint for the container which contains a custom setup script that will be run on every node on startup. See [https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup](https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup) for more information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SasToken

A container SAS token that gives access to the files. See [https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup](https://docs.microsoft.com/en-us/azure/data-factory/how-to-configure-azure-ssis-ir-custom-setup) for more information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

