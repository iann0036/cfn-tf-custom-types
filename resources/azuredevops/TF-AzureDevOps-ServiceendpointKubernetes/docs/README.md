# TF::AzureDevOps::ServiceendpointKubernetes

Manages a Kubernetes service endpoint within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ServiceendpointKubernetes",
    "Properties" : {
        "<a href="#apiserverurl" title="ApiserverUrl">ApiserverUrl</a>" : <i>String</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
        "<a href="#authorizationtype" title="AuthorizationType">AuthorizationType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>" : <i>String</i>,
        "<a href="#azuresubscription" title="AzureSubscription">AzureSubscription</a>" : <i>[ <a href="azuresubscriptiondefinition.md">AzureSubscriptionDefinition</a>, ... ]</i>,
        "<a href="#kubeconfig" title="Kubeconfig">Kubeconfig</a>" : <i>[ <a href="kubeconfigdefinition.md">KubeconfigDefinition</a>, ... ]</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>[ <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ServiceendpointKubernetes
Properties:
    <a href="#apiserverurl" title="ApiserverUrl">ApiserverUrl</a>: <i>String</i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
    <a href="#authorizationtype" title="AuthorizationType">AuthorizationType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>: <i>String</i>
    <a href="#azuresubscription" title="AzureSubscription">AzureSubscription</a>: <i>
      - <a href="azuresubscriptiondefinition.md">AzureSubscriptionDefinition</a></i>
    <a href="#kubeconfig" title="Kubeconfig">Kubeconfig</a>: <i>
      - <a href="kubeconfigdefinition.md">KubeconfigDefinition</a></i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>
      - <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ApiserverUrl

The Service Endpoint description.
- `authorization_type` - (Required) The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.
- `azure_subscription` - (Optional) The configuration for authorization_type="AzureSubscription".
- `azure_environment` - (Optional) Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
- `cluster_name` - (Required) The name of the Kubernetes cluster.
- `subscription_id` - (Required) The id of the Azure subscription.
- `subscription_name` - (Required) The name of the Azure subscription.
- `tenant_id` - (Required) The id of the tenant used by the subscription.
- `resourcegroup_id` - (Required) The resource group name, to which the Kubernetes cluster is deployed.
- `namespace` - (Optional) The Kubernetes namespace. Default value is "default".
- `cluster_admin` - (Optional) Set this option to allow use cluster admin credentials.
- `kubeconfig` - (Optional) The configuration for authorization_type="Kubeconfig".
- `kube_config` - (Required) The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.
- `accept_untrusted_certs` - (Optional) Set this option to allow clients to accept a self-signed certificate.
- `cluster_context` - (Optional) Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.
- `service_account` - (Optional) The configuration for authorization_type="ServiceAccount". This type uses the credentials of a service account currently deployed to the cluster.
- `token` - (Required) The token from a Kubernetes secret object.
- `ca_cert` - (Required) The certificate from a Kubernetes secret object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationType

The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.
- `azure_subscription` - (Optional) The configuration for authorization_type="AzureSubscription".
- `azure_environment` - (Optional) Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
- `cluster_name` - (Required) The name of the Kubernetes cluster.
- `subscription_id` - (Required) The id of the Azure subscription.
- `subscription_name` - (Required) The name of the Azure subscription.
- `tenant_id` - (Required) The id of the tenant used by the subscription.
- `resourcegroup_id` - (Required) The resource group name, to which the Kubernetes cluster is deployed.
- `namespace` - (Optional) The Kubernetes namespace. Default value is "default".
- `cluster_admin` - (Optional) Set this option to allow use cluster admin credentials.
- `kubeconfig` - (Optional) The configuration for authorization_type="Kubeconfig".
- `kube_config` - (Required) The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.
- `accept_untrusted_certs` - (Optional) Set this option to allow clients to accept a self-signed certificate.
- `cluster_context` - (Optional) Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.
- `service_account` - (Optional) The configuration for authorization_type="ServiceAccount". This type uses the credentials of a service account currently deployed to the cluster.
- `token` - (Required) The token from a Kubernetes secret object.
- `ca_cert` - (Required) The certificate from a Kubernetes secret object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `service_endpoint_name` - (Required) The Service Endpoint name.
- `apiserver_url` - (Required) The Service Endpoint description.
- `authorization_type` - (Required) The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.
- `azure_subscription` - (Optional) The configuration for authorization_type="AzureSubscription".
- `azure_environment` - (Optional) Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
- `cluster_name` - (Required) The name of the Kubernetes cluster.
- `subscription_id` - (Required) The id of the Azure subscription.
- `subscription_name` - (Required) The name of the Azure subscription.
- `tenant_id` - (Required) The id of the tenant used by the subscription.
- `resourcegroup_id` - (Required) The resource group name, to which the Kubernetes cluster is deployed.
- `namespace` - (Optional) The Kubernetes namespace. Default value is "default".
- `cluster_admin` - (Optional) Set this option to allow use cluster admin credentials.
- `kubeconfig` - (Optional) The configuration for authorization_type="Kubeconfig".
- `kube_config` - (Required) The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.
- `accept_untrusted_certs` - (Optional) Set this option to allow clients to accept a self-signed certificate.
- `cluster_context` - (Optional) Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.
- `service_account` - (Optional) The configuration for authorization_type="ServiceAccount". This type uses the credentials of a service account currently deployed to the cluster.
- `token` - (Required) The token from a Kubernetes secret object.
- `ca_cert` - (Required) The certificate from a Kubernetes secret object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpointName

The Service Endpoint name.
- `apiserver_url` - (Required) The Service Endpoint description.
- `authorization_type` - (Required) The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.
- `azure_subscription` - (Optional) The configuration for authorization_type="AzureSubscription".
- `azure_environment` - (Optional) Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
- `cluster_name` - (Required) The name of the Kubernetes cluster.
- `subscription_id` - (Required) The id of the Azure subscription.
- `subscription_name` - (Required) The name of the Azure subscription.
- `tenant_id` - (Required) The id of the tenant used by the subscription.
- `resourcegroup_id` - (Required) The resource group name, to which the Kubernetes cluster is deployed.
- `namespace` - (Optional) The Kubernetes namespace. Default value is "default".
- `cluster_admin` - (Optional) Set this option to allow use cluster admin credentials.
- `kubeconfig` - (Optional) The configuration for authorization_type="Kubeconfig".
- `kube_config` - (Required) The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.
- `accept_untrusted_certs` - (Optional) Set this option to allow clients to accept a self-signed certificate.
- `cluster_context` - (Optional) Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.
- `service_account` - (Optional) The configuration for authorization_type="ServiceAccount". This type uses the credentials of a service account currently deployed to the cluster.
- `token` - (Required) The token from a Kubernetes secret object.
- `ca_cert` - (Required) The certificate from a Kubernetes secret object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureSubscription

_Required_: No

_Type_: List of <a href="azuresubscriptiondefinition.md">AzureSubscriptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kubeconfig

_Required_: No

_Type_: List of <a href="kubeconfigdefinition.md">KubeconfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: List of <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

