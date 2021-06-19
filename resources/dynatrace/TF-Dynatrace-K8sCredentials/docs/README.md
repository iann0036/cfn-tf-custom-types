# TF::Dynatrace::K8sCredentials

CloudFormation equivalent of dynatrace_k8s_credentials

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::K8sCredentials",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#authtoken" title="AuthToken">AuthToken</a>" : <i>String</i>,
        "<a href="#certificatecheckenabled" title="CertificateCheckEnabled">CertificateCheckEnabled</a>" : <i>Boolean</i>,
        "<a href="#daviseventsintegrationenabled" title="DavisEventsIntegrationEnabled">DavisEventsIntegrationEnabled</a>" : <i>Boolean</i>,
        "<a href="#endpointurl" title="EndpointUrl">EndpointUrl</a>" : <i>String</i>,
        "<a href="#eventsintegrationenabled" title="EventsIntegrationEnabled">EventsIntegrationEnabled</a>" : <i>Boolean</i>,
        "<a href="#hostnameverification" title="HostnameVerification">HostnameVerification</a>" : <i>Boolean</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#prometheusexporters" title="PrometheusExporters">PrometheusExporters</a>" : <i>Boolean</i>,
        "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
        "<a href="#workloadintegrationenabled" title="WorkloadIntegrationEnabled">WorkloadIntegrationEnabled</a>" : <i>Boolean</i>,
        "<a href="#eventsfieldselectors" title="EventsFieldSelectors">EventsFieldSelectors</a>" : <i>[ <a href="eventsfieldselectorsdefinition.md">EventsFieldSelectorsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::K8sCredentials
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#authtoken" title="AuthToken">AuthToken</a>: <i>String</i>
    <a href="#certificatecheckenabled" title="CertificateCheckEnabled">CertificateCheckEnabled</a>: <i>Boolean</i>
    <a href="#daviseventsintegrationenabled" title="DavisEventsIntegrationEnabled">DavisEventsIntegrationEnabled</a>: <i>Boolean</i>
    <a href="#endpointurl" title="EndpointUrl">EndpointUrl</a>: <i>String</i>
    <a href="#eventsintegrationenabled" title="EventsIntegrationEnabled">EventsIntegrationEnabled</a>: <i>Boolean</i>
    <a href="#hostnameverification" title="HostnameVerification">HostnameVerification</a>: <i>Boolean</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#prometheusexporters" title="PrometheusExporters">PrometheusExporters</a>: <i>Boolean</i>
    <a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
    <a href="#workloadintegrationenabled" title="WorkloadIntegrationEnabled">WorkloadIntegrationEnabled</a>: <i>Boolean</i>
    <a href="#eventsfieldselectors" title="EventsFieldSelectors">EventsFieldSelectors</a>: <i>
      - <a href="eventsfieldselectorsdefinition.md">EventsFieldSelectorsDefinition</a></i>
</pre>

## Properties

#### Active

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateCheckEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DavisEventsIntegrationEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventsIntegrationEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameVerification

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrometheusExporters

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadIntegrationEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventsFieldSelectors

_Required_: No

_Type_: List of <a href="eventsfieldselectorsdefinition.md">EventsFieldSelectorsDefinition</a>

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

