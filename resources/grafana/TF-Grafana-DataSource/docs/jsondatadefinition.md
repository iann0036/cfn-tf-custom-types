# TF::Grafana::DataSource JsonDataDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assumerolearn" title="AssumeRoleArn">AssumeRoleArn</a>" : <i>String</i>,
    "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
    "<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>" : <i>String</i>,
    "<a href="#clientemail" title="ClientEmail">ClientEmail</a>" : <i>String</i>,
    "<a href="#connmaxlifetime" title="ConnMaxLifetime">ConnMaxLifetime</a>" : <i>Double</i>,
    "<a href="#custommetricsnamespaces" title="CustomMetricsNamespaces">CustomMetricsNamespaces</a>" : <i>String</i>,
    "<a href="#defaultproject" title="DefaultProject">DefaultProject</a>" : <i>String</i>,
    "<a href="#defaultregion" title="DefaultRegion">DefaultRegion</a>" : <i>String</i>,
    "<a href="#encrypt" title="Encrypt">Encrypt</a>" : <i>String</i>,
    "<a href="#esversion" title="EsVersion">EsVersion</a>" : <i>Double</i>,
    "<a href="#graphiteversion" title="GraphiteVersion">GraphiteVersion</a>" : <i>String</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>String</i>,
    "<a href="#loglevelfield" title="LogLevelField">LogLevelField</a>" : <i>String</i>,
    "<a href="#logmessagefield" title="LogMessageField">LogMessageField</a>" : <i>String</i>,
    "<a href="#maxidleconns" title="MaxIdleConns">MaxIdleConns</a>" : <i>Double</i>,
    "<a href="#maxopenconns" title="MaxOpenConns">MaxOpenConns</a>" : <i>Double</i>,
    "<a href="#postgresversion" title="PostgresVersion">PostgresVersion</a>" : <i>Double</i>,
    "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>,
    "<a href="#querytimeout" title="QueryTimeout">QueryTimeout</a>" : <i>String</i>,
    "<a href="#sslmode" title="SslMode">SslMode</a>" : <i>String</i>,
    "<a href="#timefield" title="TimeField">TimeField</a>" : <i>String</i>,
    "<a href="#timeinterval" title="TimeInterval">TimeInterval</a>" : <i>String</i>,
    "<a href="#timescaledb" title="Timescaledb">Timescaledb</a>" : <i>Boolean</i>,
    "<a href="#tlsauth" title="TlsAuth">TlsAuth</a>" : <i>Boolean</i>,
    "<a href="#tlsauthwithcacert" title="TlsAuthWithCaCert">TlsAuthWithCaCert</a>" : <i>Boolean</i>,
    "<a href="#tlsskipverify" title="TlsSkipVerify">TlsSkipVerify</a>" : <i>Boolean</i>,
    "<a href="#tokenuri" title="TokenUri">TokenUri</a>" : <i>String</i>,
    "<a href="#tsdbresolution" title="TsdbResolution">TsdbResolution</a>" : <i>String</i>,
    "<a href="#tsdbversion" title="TsdbVersion">TsdbVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#assumerolearn" title="AssumeRoleArn">AssumeRoleArn</a>: <i>String</i>
<a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>: <i>String</i>
<a href="#clientemail" title="ClientEmail">ClientEmail</a>: <i>String</i>
<a href="#connmaxlifetime" title="ConnMaxLifetime">ConnMaxLifetime</a>: <i>Double</i>
<a href="#custommetricsnamespaces" title="CustomMetricsNamespaces">CustomMetricsNamespaces</a>: <i>String</i>
<a href="#defaultproject" title="DefaultProject">DefaultProject</a>: <i>String</i>
<a href="#defaultregion" title="DefaultRegion">DefaultRegion</a>: <i>String</i>
<a href="#encrypt" title="Encrypt">Encrypt</a>: <i>String</i>
<a href="#esversion" title="EsVersion">EsVersion</a>: <i>Double</i>
<a href="#graphiteversion" title="GraphiteVersion">GraphiteVersion</a>: <i>String</i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
<a href="#interval" title="Interval">Interval</a>: <i>String</i>
<a href="#loglevelfield" title="LogLevelField">LogLevelField</a>: <i>String</i>
<a href="#logmessagefield" title="LogMessageField">LogMessageField</a>: <i>String</i>
<a href="#maxidleconns" title="MaxIdleConns">MaxIdleConns</a>: <i>Double</i>
<a href="#maxopenconns" title="MaxOpenConns">MaxOpenConns</a>: <i>Double</i>
<a href="#postgresversion" title="PostgresVersion">PostgresVersion</a>: <i>Double</i>
<a href="#profile" title="Profile">Profile</a>: <i>String</i>
<a href="#querytimeout" title="QueryTimeout">QueryTimeout</a>: <i>String</i>
<a href="#sslmode" title="SslMode">SslMode</a>: <i>String</i>
<a href="#timefield" title="TimeField">TimeField</a>: <i>String</i>
<a href="#timeinterval" title="TimeInterval">TimeInterval</a>: <i>String</i>
<a href="#timescaledb" title="Timescaledb">Timescaledb</a>: <i>Boolean</i>
<a href="#tlsauth" title="TlsAuth">TlsAuth</a>: <i>Boolean</i>
<a href="#tlsauthwithcacert" title="TlsAuthWithCaCert">TlsAuthWithCaCert</a>: <i>Boolean</i>
<a href="#tlsskipverify" title="TlsSkipVerify">TlsSkipVerify</a>: <i>Boolean</i>
<a href="#tokenuri" title="TokenUri">TokenUri</a>: <i>String</i>
<a href="#tsdbresolution" title="TsdbResolution">TsdbResolution</a>: <i>String</i>
<a href="#tsdbversion" title="TsdbVersion">TsdbVersion</a>: <i>String</i>
</pre>

## Properties

#### AssumeRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnMaxLifetime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomMetricsNamespaces

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultProject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EsVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GraphiteVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevelField

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMessageField

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIdleConns

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxOpenConns

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostgresVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeField

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeInterval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timescaledb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsAuthWithCaCert

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsSkipVerify

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TsdbResolution

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TsdbVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

